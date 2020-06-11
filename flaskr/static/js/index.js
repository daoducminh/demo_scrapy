function search() {
    const text = $('#search').val()
    body = {
        query: {
            match: {
                title: text
            }
        }
    }
    $.ajax({
        type: 'POST',
        url: '/search',
        beforeSend: (request) => {
            request.setRequestHeader("Access-Control-Allow-Origin", true);
        },
        data: JSON.stringify(body),
        success: (data, error) => {
            $('#result-box').empty();

            const result = data.hits.hits;
            console.log(result);

            for (let i = 0; i < result.length; i++) {
                $('#result-box').append(
                    `<div class="row news-row"><div class="col-md-1 news">${i + 1}</div>
<div class="col-md-6 news"><a href="${result[i]['_source'].url}">${result[i]['_source'].title}</a></div>
<div class="col-md-3 news">${result[i]['_source'].column}</div>
<div class="col-md-2 news">${result[i]['_score']}</div></div><hr/>`
                )
            }
            // $('#result-box')
        },
        contentType: "application/json",
        dataType: 'json'
    })
}

$('.btn-search').click(() => {
    search();
});