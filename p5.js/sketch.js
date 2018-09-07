var gather;
function preload()
{
   gather= loadJSON("studen_data.json");

}
  function setup()
  {
    noCanvas();
    var data=gather.info[1].highschool;
    createP(data);
  }
