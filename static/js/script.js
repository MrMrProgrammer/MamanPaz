function addCount() {
    var currentValue = document.getElementById("counter").innerText;
    var newValue = parseInt(currentValue) + 1;
    document.getElementById("counter").innerText = newValue;
}

function oppositeCount() {
    var currentValue = document.getElementById("counter").innerText;
    if (currentValue > 4) {
        var newValue = parseInt(currentValue) - 1;
        document.getElementById("counter").innerText = newValue;
    }
}

function addFoodToOrder(food_id) {

    var count = document.getElementById("counter").innerText;

    $.get('/order/add-to-order?food_id=' + food_id + '&count=' + count).then(res => {
        const addBtn = document.getElementById("addToOrderBtn");
        addBtn.style.display = "none";

        const successBtn = document.getElementById("success");
        successBtn.style.display = "inline-block";


        setTimeout(function () {

            const addBtn = document.getElementById("addToOrderBtn");
            const successBtn = document.getElementById("success");

            addBtn.style.display = "inline-block";
            successBtn.style.display = "none";

        }, 1000);

        console.log("ok");
    });
}

function addCommentAnswer(comment_id) {

    var answer_text = document.getElementById("answer-text").value;

    $.get('/comments/add_comment_answer?comment_id=' + comment_id + '&answer_text=' + answer_text).then(res => {
        location.reload();
    });
}

function addDate() {

    var date = document.getElementById("date").value;

    console.log(date);

    if (date != '') {
        $.get('/order/add-date?date=' + date).then(res => {
            console.log('ok');
            document.getElementById('save-date-btn').style.display = "none";
            document.getElementById('date').style.display = 'none';
            document.getElementById('show-date').innerText = 'تاریخ ثبت شده : ' + date;
            document.getElementById('show-date').style.display = 'block';

            document.getElementById('payment-not-active').style.display = 'none';
            document.getElementById('payment-active').style.display = 'inline-block';

        });
    }
}