import { useState } from "react";
import Error from "./Error";

import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import IconButton from "@mui/material/IconButton";
import InputAdornment from "@mui/material/InputAdornment";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import { useNavigate } from "react-router-dom";

import { useFormik } from "formik";
import * as yup from "yup";

const defaultTheme = createTheme();

export default function Signup({ updateCurrentUser }) {
  const navigate = useNavigate();

  const [showPassword, setShowPassword] = useState(false);
  const [errors, setErrors] = useState(null);

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const UserSchema = yup.object().shape({
    name: yup.string().required("display name is required"),
    email: yup.string().email().required("email is required"),
    password: yup
      .string()
      .min(8, "Password must be at least 8 characters")
      .required("Password is required"),
  });

  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      password: "",
    },
    validationSchema: UserSchema,
    onSubmit: (values) => {
      fetch("/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((res) => {
          if (res.ok) {
            res.json().then((data) => {
              updateCurrentUser(data);
              navigate("/");
            });
          } else {
            res.json().then((err) => setErrors(err.error));
          }
        })
        .catch((err) => setErrors("Sign up not successful, please try again"));
    },
  });

  return (
    <Container component="main" maxWidth="s">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <img
          alt="gaggle logo - let's get going"
          src="/logo-no-background.png"
          height={150}
        />
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <Box component="form" onSubmit={formik.handleSubmit} sx={{ mt: 3 }}>
          <Grid item xs={12}>
            <TextField
              required
              fullWidth
              id="name"
              label="display name"
              name="name"
              onChange={formik.handleChange}
            />
            <p style={{ color: "red" }}>{formik.errors.name}</p>
          </Grid>
          <Grid item xs={12}>
            <TextField
              required
              fullWidth
              id="email"
              label="email"
              name="email"
              onChange={formik.handleChange}
            />
            <p style={{ color: "red" }}>{formik.errors.email}</p>
          </Grid>
          <Grid item xs={12}>
            <TextField
              required
              fullWidth
              name="password"
              label="Password"
              id="password"
              onChange={formik.handleChange}
              type={showPassword ? "text" : "password"}
              InputProps={{
                endAdornment: (
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={handleClickShowPassword}
                      onMouseDown={handleMouseDownPassword}
                    >
                      {showPassword ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                ),
              }}
            />
            <p style={{ color: "red" }}>{formik.errors.password}</p>
          </Grid>
          {errors ? <Error msg={errors} /> : null}
          <Button
            color="secondary"
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Sign Up
          </Button>
          <Grid container justifyContent="flex-end">
            <Grid item>
              <Link href="/login" variant="body2">
                Already have an account? Log in
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
}
