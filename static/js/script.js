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

        }, 1500);

        console.log("ok");
    });
}


function addCommentAnswer(comment_id) {

    var answer_text = document.getElementById("answer-text").value;

    $.get('/comments/add_comment_answer?comment_id=' + comment_id + '&answer_text=' + answer_text).then(res => {

        console.log('ok')

        location.reload();

        // const addBtn = document.getElementById("addToOrderBtn");
        // addBtn.style.display = "none";
        //
        // const successBtn = document.getElementById("success");
        // successBtn.style.display = "inline-block";


        // setTimeout(function () {
        //
        //     const addBtn = document.getElementById("addToOrderBtn");
        //     const successBtn = document.getElementById("success");
        //
        //     addBtn.style.display = "inline-block";
        //     successBtn.style.display = "none";
        //
        // }, 1500);
        // console.log("ok");
    });
}