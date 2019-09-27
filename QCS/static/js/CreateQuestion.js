function handleClick() {
    getName();
    getUniqueID();
    getCourse();
    getTopics();
    getDiff();
    getSampleSolution();
    getVersion();
    getAuthor();
}

var getName = function () {
    var name = document.getElementById("name").value;
    console.log(name);
}
var getUniqueID = function () {
    var uniqueID = document.getElementById("uniqueID").value;
    console.log(uniqueID);
}
var getCourse = function () {
    var course = document.getElementById("course").value;
    console.log(course);
}
var getTopics = function () {
    var topics = document.getElementById("topics").value;
    console.log(topics);
}
var getDiff = function () {
    var diff = document.getElementById("diff").value;
    console.log(diff);
}
var getSampleSolution = function () {
    var sampleSolution = document.getElementById("sample_solution").value;
    console.log(sampleSolution);
}
var getVersion = function () {
    var version = document.getElementById("version").value;
    console.log(version);
}
var getAuthor = function () {
    var author = document.getElementById("author").value;
    console.log(author);
}