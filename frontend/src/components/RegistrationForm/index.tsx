import { Formik, Form, Field, ErrorMessage } from "formik";
import { validationSchema } from "./validationSchema";

const RegistrationForm = () => {
  const initialValues = {
    name: "",
    email: "",
    password: "",
  };

  const handleSubmit = (values: typeof initialValues) => {
    // Handle form submission
    console.log(values);
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      <Form>
        <div>
          <label>Name</label>
          <Field type="text" name="name" />
          <ErrorMessage name="name" component="div" />
        </div>
        <div>
          <label>Email</label>
          <Field type="email" name="email" />
          <ErrorMessage name="email" component="div" />
        </div>
        <div>
          <label>Password</label>
          <Field type="password" name="password" />
          <ErrorMessage name="password" component="div" />
        </div>
        <button type="submit">Register</button>
      </Form>
    </Formik>
  );
};

export default RegistrationForm;
