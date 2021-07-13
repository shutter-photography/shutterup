var i = o;
var images = [];
var time = 2000;

  //images List//

images[0] = 'sunset.jpg';
images[1] = 'waterdrop2.jpg';
images[2] = 'cats.jpg';
images[3] = 'flower.jpg';

  //Function to chane images//

function changeImg(){
  document.slide.src = images[i];

    if(i<images.length-1){
      i++;
    }else{
      i=0;
    }

    setTimeout("changeImg()",time)
  }

  window.onload = changeImg;
