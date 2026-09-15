// Helper function to get a random number with seed
function random(seed) {
    var x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
}

// Function that gets triggered when a link is clicked
// It gets a random line (which contains a link) from a text file in the data/ folder that corresponds to the topic (type) of the link
// After the link is chosen, it is opened in a new tab
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