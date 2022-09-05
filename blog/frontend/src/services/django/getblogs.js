let allBlogs = fetch('http://localhost:8000/getblogs/', {}).then((response) => response.json());

async function getBlogs() {
    const r = await fetch('http://localhost:8000/getblogs/', {}).then((response) => response.json());
    allBlogs = JSON.stringify(r);
    console.log(allBlogs);
    return;
}

export {getBlogs, allBlogs};