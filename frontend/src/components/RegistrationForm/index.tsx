import { Form, Formik, FormikHelpers } from "formik";
import { validationRegistrationSchema } from "./validationSchema";
import { Button, Grid } from "@mui/material";
import FormField, { InitialValues } from "./FormField";
import "./RegistrationForm.scss";

const RegistrationForm = () => {
  const initialValues: InitialValues = {
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
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
      validationSchema={validationRegistrationSchema}
      onSubmit={handleSubmit}
    >
      {({ touched, errors }) => {
        return (
          <Form className="registration-form">
            <Grid container spacing={2}>
              <FormField
                name="name"
                error={errors.name && touched.name}
                type=""
              />
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
              <FormField
                name="confirmPassword"
                error={errors.confirmPassword && touched.confirmPassword}
                type="password"
              />
              <Grid item xs={12} className="registration-form-item">
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  className="registration-form-button"
                >
                  Register
                </Button>
              </Grid>
            </Grid>
          </Form>
        );
      }}
    </Formik>
  );
};

export default RegistrationForm;
