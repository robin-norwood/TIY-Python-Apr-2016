console.log("Hello world!");

// Python comment:
// # a comment

// JS comment:
// // a comment

// Python:
// my_int = 5

// JavaScript:
var my_int = 5;

console.log("My int is: " + my_int);

var my_array = [1, 2, 3, 4, 5];

// Python:
// len(my_array)

// JS:
console.log("Array is: " + my_array.length)

// Python:
// ','.join(my_array)

// JS:
console.log("Array is: " + my_array.join())

// Python:
// my_dict = {'key': 5 }

var my_obj = {'key': 5 };
console.log(my_obj)

// Python
// def do_it():
//     print("Done")
//
// JS:
function do_it() {
  console.log("Done");
  console.log("sadf");
}

do_it();

var x = 5; var y = 12;


// Python:
// if x > 5:
//     print(...)

// JS:
if (x >= 5) {
  console.log("x is bigger or equal to 5");
}

// Python:
// if (x == 5 and y == 12):
//
// JS:
if (! (x == 5 && y == 12)) {
  console.log("BAH");
}


// &&   and
// ||   or
// !    not
//
// if ! x {
//   console.log("Foo");
//
// }

var x = { 'joe': function () {console.log("WHAT?!")},'bob': 5}

x.joe();
// x.mill(); // type error


// Python:
// for x in x_list:
//    stuff

//JS:

x_list = [ 1, 2, 3]

x_list.forEach( function (thing) {console.log(thing)})
