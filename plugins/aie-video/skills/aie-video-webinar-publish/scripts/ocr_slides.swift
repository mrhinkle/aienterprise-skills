import Foundation
import Vision
import CoreImage

// Vision text recognition; prints "<file>\t<top-of-frame text>" per image.
let files = Array(CommandLine.arguments.dropFirst())
for f in files {
    guard let img = CIImage(contentsOf: URL(fileURLWithPath: f)) else { continue }
    let h = VNImageRequestHandler(ciImage: img, options: [:])
    let r = VNRecognizeTextRequest()
    r.recognitionLevel = .accurate
    r.usesLanguageCorrection = true
    guard (try? h.perform([r])) != nil, let obs = r.results else { continue }
    // Vision origin is bottom-left: keep the top ~28% of the frame (slide title).
    let lines = obs.filter { $0.boundingBox.midY > 0.72 }
        .sorted { $0.boundingBox.midY > $1.boundingBox.midY }
        .compactMap { $0.topCandidates(1).first?.string }
    print("\(f)\t\(lines.joined(separator: " | "))")
}
