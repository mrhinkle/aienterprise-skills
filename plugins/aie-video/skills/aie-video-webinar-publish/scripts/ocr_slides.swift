import Foundation
import Vision
import CoreImage

// Vision text recognition; prints "<file>\t<top-of-frame text>" per image.
let files = Array(CommandLine.arguments.dropFirst())
if files.isEmpty {
    fputs("usage: ocr_slides <frame.jpg> [more.jpg ...]\n", stderr)
    exit(2)
}
var wrote = 0
for f in files {
    guard let img = CIImage(contentsOf: URL(fileURLWithPath: f)) else {
        fputs("cannot read \(f)\n", stderr)
        continue
    }
    let h = VNImageRequestHandler(ciImage: img, options: [:])
    let r = VNRecognizeTextRequest()
    r.recognitionLevel = .accurate
    r.usesLanguageCorrection = true
    guard (try? h.perform([r])) != nil, let obs = r.results else {
        fputs("vision failed \(f)\n", stderr)
        continue
    }
    // Vision origin is bottom-left: keep the top ~28% of the frame (slide title).
    let title = obs.filter { $0.boundingBox.midY > 0.72 }
        .sorted { $0.boundingBox.midY > $1.boundingBox.midY }
        .compactMap { $0.topCandidates(1).first?.string }
        .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
        .filter { !$0.isEmpty }
        .joined(separator: " | ")
    if title.isEmpty {
        fputs("no title in \(f)\n", stderr)
        continue
    }
    print("\(f)\t\(title)")
    wrote += 1
}
if wrote == 0 {
    fputs("no slide titles recognized\n", stderr)
    exit(1)
}
