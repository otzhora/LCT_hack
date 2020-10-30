import * as React from 'react';
import AceEditor from 'react-ace'
import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/theme-monokai";
const StudentPage = () => {
  return (
    <React.Fragment>
      Student Page
      <AceEditor
        mode='python'
        theme='monokai'  
      />
    </React.Fragment>
  );
}

export default StudentPage;
