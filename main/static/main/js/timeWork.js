setInterval(()=>{
    $("#time").html(formatDate(new Date()));
}, 1000);

function formatDate(date) {
    let D = date.getDay(),
        H = date.getHours();
    if (D == 0 || D == 1){
        return '<span style="color:#888888;">Выходной день</span>';
    } else if (H < 8 || H >= 17){
        return `<span style="color:#ec2929;">Закрыто</span>`;
    } else if (H == 12){
        return `<span style="color:#E65E1B;">Перерыв до 13:00</span>`;
    } else {
        return `<span style="color:#7ABE22;">Открыто до 17:00</span>`;
    }
}