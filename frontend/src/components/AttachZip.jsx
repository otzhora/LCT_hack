import * as React from 'react'

export default function ReadFromFile(props){

  let fileReader;
  
  const handleFileRead = (e)=>{
    const content = fileReader.result;
    props.onFileLoaded(content)
  }

  const handleFileChosen = (file)=>{
    fileReader = new FileReader();
    fileReader.onloadend = handleFileRead;
  }
  return <div>
    <input type='file' id='file' accept='.zip'
    onChange={e=>handleFileChosen(e.target.files[0])}/>
  </div>
}