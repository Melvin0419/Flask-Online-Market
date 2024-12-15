function addtocart(product_id){
    fetch('/addtocart',{
        method:'POST',
        body:JSON.stringify({product_id:product_id}),
    }).then((_res)=>{
        window.location.reload();
    })
}

function rmfromcart(product_id){
    fetch('/rmfromcart',{
        method:'POST',
        body:JSON.stringify({product_id:product_id}),
    }).then((_res)=>{
        window.location.reload();
    })
}

function deleteuser(user_id){
    fetch('/deleteuser',{
        method:'POST',
        body:JSON.stringify({user_id:user_id}),
    }).then((_res)=>{
        window.location.reload();
    })
}

function deleteproduct(product_id){
    fetch('/deleteproduct',{
        method:'POST',
        body:JSON.stringify({product_id:product_id}),
    }).then((_res)=>{
        window.location.reload();
    })
}

