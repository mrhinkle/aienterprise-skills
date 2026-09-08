import Foundation
import Vision
import CoreImage
import AppKit

// Uses the same foreground-instance mask Preview's "Lift Subject" uses.
let args = CommandLine.arguments
guard args.count >= 3 else { fputs("usage: liftsubject <in> <out.png>\n", stderr); exit(2) }
let inURL = URL(fileURLWithPath: args[1]), outURL = URL(fileURLWithPath: args[2])

guard let src = CIImage(contentsOf: inURL) else { fputs("cannot read input\n", stderr); exit(1) }
let handler = VNImageRequestHandler(ciImage: src, options: [:])
let req = VNGenerateForegroundInstanceMaskRequest()
do { try handler.perform([req]) } catch { fputs("vision failed: \(error)\n", stderr); exit(1) }
guard let obs = req.results?.first else { fputs("no subject found\n", stderr); exit(1) }

let pixelBuffer = try! obs.generateMaskedImage(ofInstances: obs.allInstances,
                                               from: handler, croppedToInstancesExtent: true)
let out = CIImage(cvPixelBuffer: pixelBuffer)
let ctx = CIContext()
guard let cg = ctx.createCGImage(out, from: out.extent) else { fputs("render failed\n", stderr); exit(1) }
let rep = NSBitmapImageRep(cgImage: cg)
guard let png = rep.representation(using: .png, properties: [:]) else { exit(1) }
try! png.write(to: outURL)
print("wrote \(outURL.path) \(cg.width)x\(cg.height)")
