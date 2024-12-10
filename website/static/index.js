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