// Show selected file name

const fileInput = document.querySelector('input[type="file"]');

if(fileInput){

    fileInput.addEventListener("change",function(){

        if(this.files.length>0){

            alert("Selected File : " + this.files[0].name);

        }

    });

}


// Confirm before analysis

const analyzeButton=document.querySelector("button");

if(analyzeButton){

    analyzeButton.addEventListener("click",function(){

        console.log("Analyzing student data...");

    });

}


// Highlight searched student

const searchInput=document.querySelector('input[name="search_name"]');

if(searchInput){

    searchInput.addEventListener("keyup",function(){

        this.style.borderColor="#3498db";

    });

}