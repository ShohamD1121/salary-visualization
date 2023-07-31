import React from "react";
import { Grid, TextField } from "@mui/material";
import { ErrorMessage, Field } from "formik";
import "./LoginForm.scss";

export interface InitialValues {
  email: string;
  password: string;
}

interface Props {
  name: string;
  type: string;
  error: boolean | string | undefined;
}

const FormField: React.FC<Props> = ({ name, type, error }) => {
  return (
    <Grid item xs={12} className="login-form-item">
      <Field
        as={TextField}
        label={name.charAt(0).toUpperCase() + name.slice(1)}
        name={name}
        type={type}
        fullWidth
        variant="outlined"
        margin="dense"
        helperText={<ErrorMessage name={name} />}
        error={error}
      />
    </Grid>
  );
};

export default FormField;
