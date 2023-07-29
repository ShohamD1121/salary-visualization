import { ErrorMessage, Field, Form, Formik, FormikHelpers } from "formik";
import { validationRegistrationSchema } from "./validationSchema";
import { TextField, Button, Grid } from "@mui/material";
import "./RegistrationForm.scss";

interface InitialValues {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
}

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
      {(props) => {
        const { name } = props.values;
        return (
          <Form className="registration-form">
            <Grid container spacing={2}>
              <Grid item xs={12} className="registration-form-item">
                <Field
                  as={TextField}
                  label="Name"
                  name="name"
                  fullWidth
                  variant="outlined"
                  margin="dense"
                  value={name}
                  onChange={props.handleChange}
                  onBlur={props.handleBlur}
                  helperText={<ErrorMessage name="name" />}
                  error={props.errors.name && props.touched.name}
                  required
                  sx={{
                    "& label.Mui-focused": {
                      color: "#8884d8", // Set the color when focused
                    },
                    "& .MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
                      {
                        borderColor: "#8884d8", // Set the outline color when focused
                      },
                  }}
                />
              </Grid>
              <Grid item xs={12} className="registration-form-item">
                <Field
                  as={TextField}
                  label="Email"
                  type="Email"
                  name="email"
                  fullWidth
                  variant="outlined"
                  margin="dense"
                  helperText={<ErrorMessage name="email" />}
                  error={props.errors.email && props.touched.email}
                  sx={{
                    "& label.Mui-focused": {
                      color: "#8884d8", // Set the color when focused
                    },
                    "& .MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
                      {
                        borderColor: "#8884d8", // Set the outline color when focused
                      },
                  }}
                />
              </Grid>
              <Grid item xs={12} className="registration-form-item">
                {" "}
                <Field
                  as={TextField}
                  label="Password"
                  name="password"
                  type="password"
                  fullWidth
                  variant="outlined"
                  margin="dense"
                  helperText={<ErrorMessage name="password" />}
                  error={props.errors.password && props.touched.password}
                  sx={{
                    "& label.Mui-focused": {
                      color: "#8884d8", // Set the color when focused
                    },
                    "& .MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
                      {
                        borderColor: "#8884d8", // Set the outline color when focused
                      },
                  }}
                />
              </Grid>

              <Grid item xs={12} className="registration-form-item">
                <Field
                  as={TextField}
                  label="Confirm Password"
                  name="confirmPassword"
                  type="password"
                  fullWidth
                  variant="outlined"
                  margin="dense"
                  helperText={<ErrorMessage name="confirmPassword" />}
                  error={
                    props.errors.confirmPassword &&
                    props.touched.confirmPassword
                  }
                  sx={{
                    "& label.Mui-focused": {
                      color: "#8884d8", // Set the color when focused
                    },
                    "& .MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
                      {
                        borderColor: "#8884d8", // Set the outline color when focused
                      },
                  }}
                />
              </Grid>

              <Grid item xs={12} className="registration-form-item">
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  className="registration-form-button"
                  sx={{
                    backgroundColor: "#8884d8",
                    "&:hover": {
                      backgroundColor: "#a5a2e0", // Set the lighter hover color
                    },
                  }}
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
