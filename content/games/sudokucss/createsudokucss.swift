import Foundation



func convertPuzzle(initialPuzzle: String) -> [[Int]] {
	let oldPuzzle = initialPuzzle.replacingOccurrences(of: ".", with: "0")
	var puzzle: [[Int]]
	puzzle = [[],[],[],[],[],[],[],[],[]]
	for iiii in 0..<9 {
		for iii in 0..<9 {
			let index = iii+9*iiii
			let sIndex = oldPuzzle.index(oldPuzzle.startIndex, offsetBy: index)
			var piece: Int!
			piece = Int(String(oldPuzzle[sIndex]))
			puzzle[iiii].append(piece)
		}
	}
	return puzzle
}




var allPuzzles: String
allPuzzles = """
9.5...2.4..2...5...6.7.5.1....689....2..3..9.73.....48..4...8..6...5...9..7...4..,
...691.............92...34.6.9...4.8..42.95...5.....2..4.1.5.7....7.3....3..4..5.,
.1.9.6.7...........751.426....3.9...9...8...47.3.5.6.2...8.5.......1.....68...52.,
89.1.4.53...7.8....412.369..6.9.2.8....6.5.......1....6...4...9.15...34...7...8..,
.2.615.7..96.7.58.....4................458.....57.28..94.....588..5.1..3..2...7..,
.4.....9.....5....51..4..62.3.....8..9.2.6.5..57...63...3...8..4..387..67...1...5,
...9.3...3...1...5...5.8...47.1.9.8683.....946.......7..3...6..59..7..3114.....28,
.........6..759..3.24...97.5...3...243..6..91..6...5...7..1..4..........8.15.23.7,
96.....28.81...56.7...1...3....9.......724......638....3.9.5.7.6.......5.42...98.,
...5.7.....7.4.1..15.8.2.699...7...67..1.4..8....6.............4.9...8.2382...675,
.3.....4.14.....78.258.469..56.3.41.87.....65....2.....6..5..8..9.3.2.5....1.6...,
.........8.93.51.6.25.7.34.78..6..242.......1...2.1.......5.....5.7.4.1.4.6.1.7.9,
....6....4..982..7..81.49...35...71.2.6...3.971.3.5.62..........4.216.7..2.....4.,
79.....212..839..7....2....4.5...7.9.7.....5...6...2....4...6...1.5.3.8..3..6..4.,
.5..2..1...........834.579..72...98..4.6.9.3...62.71......5....16.....58...9.8...,
4.8...3.52..8.5..9.7..4..6.64.9.3.51..2...4..98.....76....6.......2.4......1.7...,
.816.759...9.2.8..7.......3..67583...4.3.9.5............2...4...731.596.....9....,
...3.4....52.6.84..4.....6..6..3..5.....7....17.5.6.9898.2.1.75.2.....1..........,
..67.13....1...8....9.6.2......7....9.......7.6.4.9.8.2..895..3.8..3..2...4...5..,
8.1...2.97.......5...315....798.634...........4..2..6.6.7...9.8....9.......732...,
1...6...5.79.1.82..58...37....127...23.6.4.18.........9..8.5..3..5.9.1...........,
6.3.4.8.1....6.....1.2.8.7....5.7.......9......2...5..5..3.6..8.3..1..9..7.8.9.4.,
....9.....1.....5..572.418............3.8.6..54..3..91..5.1.8...9.6.8.1..61.2.47.,
84..7..19..3...2...9.....8.6..5.9..7............4.1....8.7.6.4.9.5...1.22...1...6,
..26.54..5..4.1..6..4...3...29...57.....6.....8..5..6..562.871..4..7..9..3.....4.,
"""
allPuzzles = allPuzzles.replacingOccurrences(of: "\n", with: "")
let puzzleArray = allPuzzles.components(separatedBy: ",")
for i in 0..<25 {
	var startStr = "---\ntitle: 'Sudoku - Just CSS/HTML'\ndescription: 'Complete a sudoku puzzle without Javascript or server-side interaction.'\ngametype: 'simple'\ngameid: "+String(i+1)+"\ndate: 2018-06-20\ntags: []\ndraft: false\ntype: 'games'\nnum19: [{'idx':1,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':2,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':3,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':4,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':5,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':6,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':7,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':8,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]},{'idx':9,'arr1':[1,2,3,4,5,6,7,8,9],'arr2':[1,2,3,4,5,6,7,8,9]}]\npuzzle: "
	startStr += convertPuzzle(initialPuzzle: puzzleArray[i]).description
	startStr += "\nlayout: 'sudokucssstatic'\n---"
	print(i)
	do {
    // get the documents folder url
    if let documentDirectory = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
        // create the destination url for the text file to be saved
        let fileURL = documentDirectory.appendingPathComponent("sudokucss/simple"+String(i+1)+".md")
        // define the string/text to be saved
        let text = startStr
        // writing to disk
        try text.write(to: fileURL, atomically: false, encoding: .utf8)
        print("saving was successful")
        // any code posterior code goes here
        // reading from disk
        let savedText = try String(contentsOf: fileURL)
    }
	} catch {
		print("error:", error)
	}
	
	
}