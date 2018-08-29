import React from 'react';
import ReactDOM from 'react-dom';
import PostsList from './api_get';


function Main(props) {
  return (
        <div>
            <h1>POSTS LIST</h1>
            <PostsList />
        </div>
        );
}
                    

ReactDOM.render(<Main />,
               document.getElementById('root')
);