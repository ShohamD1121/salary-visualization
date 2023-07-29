import { Formik, Form, FormikHelpers, Field, ErrorMessage } from "formik";
import { validationLoginSchema } from "./validationSchema";
import { Button, Grid, TextField } from "@mui/material";
import "./LoginForm.scss";

interface InitialValues {
  email: string;
  password: string;
}

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
      {(props) => (
        <Form className="login-form">
          <Grid container spacing={2}>
            <Grid item xs={12} className="login-form-item">
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
            <Grid item xs={12} className="login-form-item">
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
            <Grid item xs={12} className="login-form-item">
              <Button
                type="submit"
                variant="contained"
                color="primary"
                className="login-form-button"
                sx={{
                  backgroundColor: "#8884d8",
                  "&:hover": {
                    backgroundColor: "#a5a2e0", // Set the lighter hover color
                  },
                }}
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
