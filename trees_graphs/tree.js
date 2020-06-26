// practicing trees in JavaScript
"use strict";

// make a tree class
class Tree {
    constructor(data) {
        this.data = data;
        this.children = [];
    }

    printTree() {
        // print all the nodes in a tree, depth first.

        let toVisit = [this];
        console.log("toVisit:");
        console.log(toVisit);
        console.log(toVisit == true);
        console.log(toVisit == false);
        console.log(toVisit.length);

        while (toVisit.length > 0) {
            let current = toVisit.pop();
            // console.log("\n\ncurrent");
            console.log(current);

            // console.log("\n\ntoVisit");
            // console.log(toVisit);
            for (const child of current.children) {
                toVisit.push(child);
            }
            // console.log("\n\ntoVisit");
            // console.log(toVisit);
        }
    }
};

// make a tree 
let myTree = new Tree('base', []);

// create and add children
let myChild1 = new Tree('child1', []);
let myChild2 = new Tree('child2', []);

myTree.children.push(myChild1);
myTree.children.push(myChild2);

//create and add grand children
let myGrandChild1 = new Tree('grandchild1', []);

myChild1.children.push(myGrandChild1);

console.log("\n\n'myTree:'");
console.log(myTree);
console.log("\n\n'myTree.printTree:'");
console.log(myTree.printTree());

// traverse a tree