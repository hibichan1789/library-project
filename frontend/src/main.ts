const apiUrl = import.meta.env.VITE_API_URL;

console.log(apiUrl)

interface Book{
  id:number,
  title:string,
  author:string,
  description?:string;
}
async function getBooks(){
  const readBookUrl = `${apiUrl}/books`
  try{
    const response = await fetch(readBookUrl);
    if(!response.ok){
      const errorMessage = await response.text();
      console.error(errorMessage);
      throw new Error(errorMessage);
    }
    const Books:Book[] = await response.json()
    return Books
  }
  catch(error){
    console.error(String(error));
  }
}

const books = await getBooks();
console.log(books);