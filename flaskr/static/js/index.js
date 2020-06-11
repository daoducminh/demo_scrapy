$('.btn-search').click(() => {
    const text = $('#search').val()
    // $.post('/elastic-search/movie', { keyword: text }, (data, status) => {
    //     console.log(data);
    //     $('#result-box').empty();
    //     const arr = data.suggest.suggest1[0].options;
    //     for (let i = 0; i < arr.length; i++) {
    //         $('#result-box').append(`<p>${arr[i]._source.name}</p>`)
    //     }
    // })
    console.log('clicked');
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
                    `<div class="col-md-7">${result[i]['_source'].title}</div>
<div class="col-md-3">${result[i]['_source'].column}</div>
<div class="col-md-2">${result[i]['_score']}</div>`
                )
            }
            // $('#result-box')
        },
        contentType: "application/json",
        dataType: 'json'
    })
});