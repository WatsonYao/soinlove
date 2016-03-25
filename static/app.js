import React from 'react';

var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello, Mathilda! I am a Watson.
      </div>
      
    );
  }
});

ReactDOM.render(
  <CommentBox />,
  document.getElementById('content')
);
