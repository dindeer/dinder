var gather;
function preload()
{
   gather= loadJSON("webscrapping/student_content2020.json");
   nome=   loadJSON("webscrapping/name_2020.json");
   //console.log(nome);


}
  function setup()
  {
    noCanvas();

    var data=gather.content[1].HighSchool;
    var name=nome.infor[1].name;
    //createP(name);
   //createP(data);
   var loop = nome.infor;
   var con = gather.content;

   for(var i =0;i<loop.length;i++)
   {
     createElement('h2',loop[i].name);
     //createElement('h2',con[j+1].HighSchool)

   }
  }
