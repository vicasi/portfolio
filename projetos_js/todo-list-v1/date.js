function getDate(){
    let getD = new Date();
    let options = {
        weekday: 'long',
        year: 'numeric',
        era: 'long',
    };

    let day = getD.toDateString('en-US', options);
    return day
}

module.exports.getdate = getDate

function getDay() {
    let today = new Date()
    let options = {weekday:'long'}
    return today.toLocaleDateString('en-US', options)
}

module.exports.getday = getDay