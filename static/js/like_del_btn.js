
    const likeBtns = document.querySelectorAll('.like-btn')
    for (i=0;i<likeBtns.length;i++){
        likeBtns[i].addEventListener('click',(e)=>{
            console.log('a')
            e.preventDefault()
            const arr = e.target.parentNode.children[4].innerText.split(' ')
            const number = parseInt(arr[arr.length - 1])
            const paint_id = e.target.parentNode.dataset.id
            $.ajax({
                type:"POST",
                url:`http://localhost:8000/api/paints/like/${paint_id}`,
                success : function(json) {
                    if (json.msg == 'delete'){
                        e.target.parentNode.children[4].innerText = `liked : ${number - 1}`
                    } else if (json.msg == 'ok') {
                        e.target.parentNode.children[4].innerText = `liked : ${number + 1}`
                    } else {
                        alert(json.msg)
                    }
                }
                });
        })
    }
    
    const delBtns = document.querySelectorAll('.del-btn')
    for (i=0;i<delBtns.length;i++){
        delBtns[i].addEventListener('click',(e)=>{
            e.preventDefault()
            const paint_id = e.target.parentNode.dataset.id
            $.ajax({
                type:"DELETE",
                url:`http://localhost:8000/api/paints/delete/${paint_id}`,
                success : function(json) {
                    if (json.msg == 'delete') {
                        alert('게시물이 삭제되었습니다.')
                        window.location.reload()
                    } else if (json.msg == 'err-user') {
                        alert('삭제 권한이 없습니다.')
                    } else if (json.msg == 'not founded') {
                        alert('게시물이 존재하지 않습니다.')
                    }
                }
                });
        })
    }
