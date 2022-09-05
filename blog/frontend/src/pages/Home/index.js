import React, {useState, useEffect} from 'react';
import axios from 'axios';
import tryLogin from '../../services/django/login';

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

const HomePage = () => {
    const [blogs, setBlogs] = useState([]);
    const username = getCookie('username');
    const password = getCookie('password');
    const [check, setCheck] = useState(false);
    tryLogin(username, password).then((status)=>{setCheck(status);console.log(check)});
    console.log(check);
    useEffect(()=>{
        fetch('http://localhost:8000/getblogs/', {
        })
        .then((response) => response.json())
        .then((data)=>{
            setBlogs(data);
        });
    },[]);
    return(
        <div>
            <h1>Home Page</h1>
            <button onClick={async()=>{
                document.cookie=`username=${null};secure`;
                document.cookie=`password=${null};secure`;
                document.location = '/';
            }}>Logout</button>
            <div id='blogs'>{blogs.map((blog)=>{
                return(
                    <div key={blog['pk']}>
                        <div id={blog['pk'].toString() + "data"}>
                            <h2>{blog['fields']['title']}</h2>
                            <p>{blog['fields']['content']}</p>
                        </div>
                        <div id={blog['pk'].toString() + "delete"}>
                            <button onClick={async()=>{
                                const response = await axios.post('http://localhost:8000/delete/', {
                                    "pk": blog['pk'].toString(),
                                    "username": getCookie('username'),
                                    "password": getCookie('password')
                                })
                                alert(response.data);
                                document.location = '/main';
                            }}>
                                Delete
                            </button>
                        </div>
                    </div>

                )
            })}</div>
            <div id="new">
                <h2>New Blog</h2><br></br>
                <input type="text" id="new-title" placeholder="Title"></input><br></br>
                <input type="text" id="newcontent" placeholder="Content"></input><br></br>
                <button onClick={async()=>{
                    const title = document.getElementById('new-title').value;
                    const content = document.getElementById('newcontent').value;
                    const response = await axios.post('http://localhost:8000/add/', {
                        "name": getCookie('username'),
                        "title": title,
                        "content": content,
                        "username": getCookie('username'),
                        "password": getCookie('password')
                    });
                    console.log(response);
                    if (response['data'] === 'Blog added successfully') {
                        alert("Blog added");
                        window.location.reload();
                    }
                    else {
                        alert("Error...\nBlog not added\nTry logging out and in if issue persists");
                    }
                }}>Add</button>
            </div>
        </div>
    )
}

export default HomePage;