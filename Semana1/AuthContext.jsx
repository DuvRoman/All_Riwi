import React from 'react'
import { useState, useEffect, createContext, useContext } from 'react'

export default function AuthContext() {

    let [user, setUserState] = useState(null);
    let [loading, setLoadingState] = useState(false);

    useEffect(()=> {
        //Verificar si hay un usuario en el Local Storage

        let storedUser= localStorage.getItem("userData")
        if(storedUser){
            setUserState(JSON.parse(storedUser))
        }
        setLoadingState(false)

    }, [])


  return (
    <div>AuthContext</div>
  )
}
