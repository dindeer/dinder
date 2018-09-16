var gather;
function preload()
{
   gather= loadJSON("webscrapping/student_content2020.json");


}
  function setup()
  {
    noCanvas();
    var data=gather.content[1].HighSchool[1];
    createP(data);
  }
