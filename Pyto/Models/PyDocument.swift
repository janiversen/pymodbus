//
//  PyDocument.swift
//  Pyto
//
//  Created by Adrian Labbe on 9/8/18.
//  Copyright © 2018 Adrian Labbé. All rights reserved.
//

#if os(iOS)
import UIKit

typealias Document = UIDocument
#else
import Cocoa

typealias Document = NSDocument
#endif

/// Errors opening the document.
enum PyDocumentError: Error {
    case unableToParseText
    case unableToEncodeText
}

/// A document representing a Python script.
class PyDocument: Document {
    
    /// The text of the Python script to save.
    var text = ""
    
    /// Checks for conflicts and presents an alert if needed.
    ///
    /// - Parameters:
    ///     - completion: Code to call after the file is checked.
    func checkForConflicts(completion: (() -> Void)?) {
        #if MAIN
        if documentState == UIDocument.State.inConflict, let versions = NSFileVersion.unresolvedConflictVersionsOfItem(at: fileURL), versions.count > 1 {
            
            guard let resolver = UIStoryboard(name: "ConflictsResolver", bundle: Bundle.main).instantiateInitialViewController() as? ResolveConflictsTableViewController else {
                completion?()
                return
            }
            
            resolver.document = self
            resolver.versions = versions
            resolver.completion = completion
            
            let navVC = UINavigationController(rootViewController: resolver)
            navVC.modalPresentationStyle = .formSheet
            
            UIApplication.shared.keyWindow?.topViewController?.present(navVC, animated: true, completion: nil)
        } else {
            completion?()
        }
        #else
        completion?()
        #endif
    }
    
    private func load(contents: Any) throws {
        guard let data = contents as? Data else {
            // This would be a developer error.
            fatalError("*** \(contents) is not an instance of NSData.***")
        }
        
        guard let newText = String(data: data, encoding: .utf8) else {
            throw PyDocumentError.unableToParseText
        }
        
        text = newText
    }
    
    private func makeData() throws -> Data {
        guard let data = text.data(using: .utf8) else {
            throw PyDocumentError.unableToEncodeText
        }
        return data
    }
    
    #if os(iOS)
    
    override func contents(forType typeName: String) throws -> Any {
        
        do {
            return try makeData()
        } catch {
            throw error
        }
    }
    
    override func load(fromContents contents: Any, ofType typeName: String?) throws {
        do {
            try load(contents: contents)
        } catch {
            throw error
        }
    }
    
    #else
    
    override func makeWindowControllers() {
        // Returns the Storyboard that contains your Document window.
        let storyboard = NSStoryboard(name: NSStoryboard.Name("Main"), bundle: nil)
        let windowController = storyboard.instantiateController(withIdentifier: NSStoryboard.SceneIdentifier("Document Window Controller")) as! NSWindowController
        if !windowController.isWindowLoaded {
            windowController.loadWindow()
        }
        (windowController.contentViewController as? EditorViewController)?.document = self
        self.addWindowController(windowController)
    }
    
    override func data(ofType typeName: String) throws -> Data {
        
        do {
            return try makeData()
        } catch {
            throw error
        }
    }
    
    override func read(from data: Data, ofType typeName: String) throws {
        
        do {
            try load(contents: data)
        } catch {
            throw error
        }
    }
    
    #endif
}
