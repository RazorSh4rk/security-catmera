let d = new DrawJS('c')

function train(){
    const r = document.getElementById('train-res')
        n = document.getElementById('name')
    r.innerHTML = 'video feed will freeze while training' +
                    '<br>please move your head thanks :3'
    fetch('http://localhost:5000/train?name=' + (n.value?n.value:'razor'))
    .then((resp) => resp.json())
    .then((res) => {
        r.innerHTML = 'new face trained :3c'
    })

    setTimeout(()=>r.innerHTML='', 3000)
}

function cat(x,y,w,h){

    d.circle(x, y, w, 'yellow', true)
    var ear0=[
        new Vertex(x-10, y-80),
        new Vertex(x-50, y-130),
        new Vertex(x-80, y)
    ]
    var ear1=[
        new Vertex(x+10, y-80),
        new Vertex(x+50, y-130),
        new Vertex(x+80, y)
    ]
    
    //Draw the ears
    d.polygon(ear0, 'yellow', true)
    d.polygon(ear1, 'yellow', true)
    
    //Draw the kawaii anime eyes (✧ω✧)
    d.circle(x-40, y-20, 15, 'black', true)
    d.point(x-50, y-25, 'white')
    d.circle(x+40, y-20, 15, 'black', true)
    d.point(x+30, y-25, 'white')
}


setInterval(() => {
	fetch('http://localhost:5000/faces')
	.then((res) => res.json())
	.then((obj) => {
		d.getContext().clearRect(0,0,640,480)
	    obj.forEach((data) => {
	       let data2 = JSON.parse(data)
	       let centerx = data2.x + (data2.w/2)
	       let centery = data2.y + (data2.w/2)
	       cat(centerx, centery, data2.w/2, data2.h/2) 
	       d.write(data2.name, data2.x, data2.y, 'white', true, '20px Arial')
	    })
	})
}, 300)