import AppBar from 'material-ui/lib/app-bar';

var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello, Mathilda! I am a Watson.
        <AppBar
        title="Title"
        iconClassNameRight="muidocs-icon-navigation-expand-more"
        />
      </div>
      
    );
  }
});

ReactDOM.render(
  <CommentBox />,
  document.getElementById('content')
);
