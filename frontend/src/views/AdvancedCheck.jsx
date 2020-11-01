import React, {useState, useRef} from 'react'
import Async from 'react-async';

function createAdvanceOut(setup, checks, run){
  return <div>
    <h5>Setup</h5>
    <div>{setup}</div>
    <h5>Checks</h5>
    <div>{checks}</div>
    <h5>Checks</h5>
    <div>{run}</div>
  </div>

}
const AdvancedCheck = (props) => {
  const [url, setUrl] = useState('https://github.com/otzhora/Algorithms');
  const [data, setData] = useState(undefined);
  const divRef = useRef(null);
  async function renderCheck(){
    console.log(url)
    const res = await fetch(`http://localhost:8000/advanced/`,{
      method: 'POST',
      body: JSON.stringify({
        'git_url': url,
      })
    })
      .then(res => (res.ok ? res : Promise.reject(res)))
      .then(res => res.json())
      .then(res=>{
        console.log(res); 
        setData(res);
      })
  }
  return (
    <div display="inline" width={"50px"}>
      <input type='text' onValueChange={setUrl} value={url}/>
      <button onClick={renderCheck}>Submit</button>
      {data ? createAdvanceOut(data.setup, data.checks, data.run) : null}
      
    </div>
  );
}

export default AdvancedCheck;