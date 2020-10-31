import * as React from 'react'

export default function ReadFromFile(){
  let fileReader;
  const handleFileRead = (e)=>{
    const content = fileReader.result;
    console.log(content);
  }

  const handleFileChosen = (file)=>{
    fileReader = new FileReader();
    fileReader.onloadend = handleFileRead;
    fileReader.readAsText(file);
  }
  return <div>
    <input type='file' id='file' accept='.py'
    onChange={e=>handleFileChosen(e.target.files[0])}/>
  </div>
}