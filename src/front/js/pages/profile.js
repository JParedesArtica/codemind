import React, { useState, useContext, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Context } from "../store/appContext";

export const Profile = () => {
    const [selectedTeacher, setSelectedTeacher] = useState({
        id: null,
        firstName: null,
        lastName: null
    });;
    const [showAlert, setShowAlert] = useState(false);
    const { store, actions } = useContext(Context);
    const initialFormData = {
        id: store.user.id,
        firstName: store.user.firstName,
        lastName: store.user.lastName,
        email: store.user.email,
        teacher: store.user.teacher ? parseInt(store.user.teacher) : null,
        img: store.user.img
    };
    const [formData, setFormData] = useState({ ...initialFormData });


    const handleTeacherSelect = (teacher, e) => {
        e.preventDefault(); // Prevenir desplazamiento automático
        setSelectedTeacher({
            id: parseInt(teacher.id),
            firstName: teacher.firstName,
            lastName: teacher.lastName
        })
        setFormData({ ...formData, teacher: teacher.id });

    };

    const handleChange = (e) => {
        const { name, value } = e.target;

        // Realiza la transformación de la primera letra en mayúscula
        const updatedValue =
            name === "firstName" || name === "lastName"
                ? value
                    .split(" ")
                    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
                    .join(" ")
                : value;

        const updatedFormData = { ...formData, [name]: updatedValue };
        setFormData(updatedFormData);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const baseUrl = "https://ui-avatars.com/api";
            const size = 200; // Tamaño del avatar (píxeles)
            const rounded = true; // Forma redondeada
            const background = "random"; // Color de fondo aleatorio
            const name = formData.firstName + " " + formData.lastName
            const imgURL = `${baseUrl}/?name=${encodeURIComponent(name)}&size=${size}&rounded=${rounded}&background=${background}`
            const updatedFormData = { ...formData, img: imgURL, teacher: selectedTeacher.id  };
            console.log(updatedFormData)
            await actions.updateUser(updatedFormData);
            setShowAlert(true);
        } catch (error) {
            console.error('Error al actualizar el usuario: ', error)
        }
    };

    useEffect(() => {
        if (store.user.teacher && store.teachers) {
            const assignedTeacher = store.teachers.find(
                teacher => teacher.id === parseInt(store.user.teacher)
            );
            if (assignedTeacher) {
                setSelectedTeacher({
                    id: assignedTeacher.id,
                    firstName: assignedTeacher.firstName,
                    lastName: assignedTeacher.lastName
                });
            }
        }
    }, [store.user.teacher, store.teachers]);






    return (
        <div className="container vh-100 align-items-center">
            <div className="row mb-4">
                <div className="col">
                    <Link to="/modules"><i className="fa-solid fa-arrow-left arrow-back"></i></Link>
                </div>
            </div>
            <div className="row justify-content-center d-flex justify-content-between">
                <div className="col-sm-12 col-md-6 text-start">
                    <div className="embed-responsive embed-responsive-16by9">
                        <h2 className='bigtext text-line text-break'>
                            Hi <span className='text-color-primary'>{store.user.firstName}</span>! This is your profile
                        </h2>
                    </div>
                </div>
                <div className="col-sm-12 col-md-6 mt-4 align-items-start">

                    {showAlert && (
                        <div className="alert alert-success alert-dismissible fade show" role="alert">
                            User updated successfully!
                            <button type="button" className="btn-close" onClick={() => setShowAlert(false)}></button>
                        </div>
                    )}
                    <form onSubmit={handleSubmit}>
                        <div className='d-flex justify-content-between mb-2'>
                            <p className='my-0 me-4'>First Name:</p>
                            <input type="text" className="form-control" id="firstName" name="firstName" value={formData.firstName} onChange={handleChange} style={{ maxWidth: "60%" }}></input>
                        </div>
                        <div className='d-flex justify-content-between  mb-2'>
                            <p className='my-0 me-4'>Last Name:</p>
                            <input type="text" className="form-control" id="lastName" name="lastName" value={formData.lastName} onChange={handleChange} style={{ maxWidth: "60%" }}></input>
                        </div>
                        <div className='d-flex justify-content-between  mb-2'>
                            <p className='my-0 me-4'>E-mail:</p>
                            <input type="text" className="form-control" id="email" name="email" value={formData.email} onChange={handleChange} style={{ maxWidth: "60%" }}></input>
                        </div>
                        <div className='d-flex justify-content-between  mb-2'>
                            <p className='my-0 '>Teacher:</p>
                            <div className="h-25 px-5  ">
                                <div className="btn-group dropdown-center" >
                                    <button className="btn btn-secondary dropdown-toggle " type="button" data-bs-toggle="dropdown" aria-expanded="false" disabled={!!store.user.teacher} >
                                        {selectedTeacher.firstName && selectedTeacher.lastName
                                            ? `${selectedTeacher.firstName} ${selectedTeacher.lastName}`
                                            : "Select Your Teacher"}
                                    </button>
                                    <ul className="dropdown-menu dropdown-menu-dark">
                                        {store.teachers && store.teachers.map((teacher, index) => (
                                            <li key={index}>
                                                <p className="dropdown-item" onClick={(e) => handleTeacherSelect(teacher, e)}>
                                                    {teacher.firstName + " " + teacher.lastName}
                                                </p>
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="row  align-items-center mt-4 justify-content-end">
                            <div className=" col-sm-12 col-md-6  text-center">
                                <button type="submit" className="btn btn-primary">
                                    Update User
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div className='row h-25 d-flex justify-content-end align-items-center'>
                <div className="col-sm-1 col-md-4  text-sm-end justify-content-between">
                    <div className="d-flex justify-content-between ">
                        <Link to={"/changepassword"}><a href="#" className="btn btn-outline-secondary">Change password</a></Link>
                        <Link to={"/iamteacher"} className="">I'm Professor</Link>
                    </div>
                </div>
            </div>
        </div>
    );
};
