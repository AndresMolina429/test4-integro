import { useState } from 'react'
import './App.css'
import axios from 'axios'
import toast, { Toaster } from 'react-hot-toast';
import { useForm } from 'react-hook-form'


function App() {
  const [input, setInput] = useState('')
  const { register, handleSubmit, formState: {
    errors
  } } = useForm()
  const notify = (text) => toast(text);

  const onSubmit = handleSubmit(data => {
     axios.post(`http://127.0.0.1:8000/test4/`, data )
      .then((res) => { 
        let text = 'La Frase no es un palindromo'
        if (res.data.state) {
          text = 'La Frase si es un palindromo'
        }
        notify(text)
      })
      .catch((err) => console.log(err))
  })

  return (
    <>
      <form className='container' onSubmit={onSubmit}>
        <input type='text' id='phrase' className='input' name='phrase' onChange={e => setInput(e.target.value)} 
        { ...register('phrase', { required: true }) }
        />
        <Toaster/>
        <button type="submit" className='button'>Consultar</button>
      </form>
        {errors.phrase && <span>Ingrese Frase a verificar</span>}
    </>
  )
}

export default App
