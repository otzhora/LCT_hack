import React from 'react'
import Async from 'react-async';

const loadTaskText = async ({name}) =>
    fetch(`http://localhost:8000/task/${name}`)
      .then(res => (res.ok ? res : Promise.reject(res)))
      .then(res => res.json())

const TaskStatement = (props) => {
  
  return (
    <div display="inline" width={"50px"}>
      <Async promiseFn={loadTaskText} name={props.name}>
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
      </Async>
    </div>
  );
}

export default TaskStatement;
