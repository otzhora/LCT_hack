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
        divRef.current = createAdvanceOut(...res)
      })
  }
  return (
    <div display="inline" width={"50px"}>
      <input type='text' onValueChange={setUrl} value={url}/>
      <button onClick={renderCheck}>Submit</button>
      <div ref={divRef}></div>
      {/* <Async promiseFn={loadTaskText} name={props.name}>
        {({ data, err, isLoading }) => {
          if (isLoading) return "Loading..."
          if (err) return `Something went wrong: ${err.message}`

          if (data)
            return (
              <div>
                <h1>{data.task.title}</h1>
                {data.task.task}
                Teacher id
                {data.task.teacher_id}
              </div>
            )
        }}
      </Async> */}
    </div>
  );
}

export default AdvancedCheck;