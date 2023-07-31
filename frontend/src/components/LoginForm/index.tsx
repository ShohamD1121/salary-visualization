import { Formik, Form, FormikHelpers } from "formik";
import { validationLoginSchema } from "./validationSchema";
import { Button, Grid } from "@mui/material";
import FormField, { InitialValues } from "./FormField";
import "./LoginForm.scss";

const LoginForm = () => {
  const initialValues: InitialValues = {
    email: "",
    password: "",
  };

  const handleSubmit = (
    values: InitialValues,
    formikHelpers: FormikHelpers<InitialValues>
  ) => {
    console.log(values);
    formikHelpers.resetForm();
  };
  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationLoginSchema}
      onSubmit={handleSubmit}
    >
      {({ touched, errors }) => (
        <Form className="login-form">
          <Grid container spacing={2}>
            <FormField
              name="email"
              error={errors.email && touched.email}
              type="email"
            />
            <FormField
              name="password"
              error={errors.password && touched.password}
              type="password"
            />
            <Grid item xs={12} className="login-form-item">
              <Button
                type="submit"
                variant="contained"
                color="primary"
                className="login-form-button"
              >
                Login
              </Button>
            </Grid>
          </Grid>
        </Form>
      )}
    </Formik>
  );
};

export default LoginForm;
