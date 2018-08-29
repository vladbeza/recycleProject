var React = require('react')
var ReactDOM = require('react-dom')
import axios from 'axios';

class PostsList extends React.Component{

    constructor(props) {
    super(props);
    this.state = {
      postContent: []
        }
    };

    componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/v0/news_all/").then(response => {
            console.log(response);
            this.setState({postContent: response.data});
        });
    };


    render() {
        const posts = this.state.postContent.map((postData) => {
        return (
                <div className="all_posts">
                    <h1>{postData.title}</h1>
                    <img src={postData.short_image} />
                    <p className="post-meta"><small>{postData.author.nick_name}</small></p>
                    <p className="post-meta"><small>{postData.pub_date}</small></p>
                </div>
                )});
        return (
                <div className="Posts">
                    {posts}
                </div>);
    };
}


export default PostsList