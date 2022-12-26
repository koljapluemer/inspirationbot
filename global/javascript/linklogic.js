// the logic that chooses a random link when clicking an a tag

function random(seed) {
    var x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
}
function getRandomLink(type) {
    file_name = "/global/data/" + type + ".txt";
    console.log('File Name', file_name)
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file_name, false);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status == 0) {
                var allText = rawFile.responseText;
                var lines = allText.split("\n");
                // var randomLine = lines[Math.floor(Math.random() * lines.length)];
                // use random function with current date (in yyyymmdd format)
                // get current Date - 4 hours (to have the picture switch at 4am)
                date = new Date() - 14400000;
                date = new Date(date);
                date = date.getFullYear() + "" + (date.getMonth() + 1) + "" + date.getDate();
                var randomLine = lines[Math.floor(random(date) * lines.length)];
                line_list = randomLine.split(" ");
                link = line_list[0];
                console.log('Link', link)
                window.open(link, '_blank');
            }
        }
    }
    rawFile.send(null);
    return false;

}