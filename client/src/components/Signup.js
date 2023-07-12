import { useState } from "react";

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

import Error from "./Error";

const defaultTheme = createTheme();

export default function Signup({ currentUser, updateCurrentUser }) {
  const navigate = useNavigate();

  if (currentUser) {
    navigate("/");
  }
  const [showPassword, setShowPassword] = useState(false);
  const [errors, setErrors] = useState(null);

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const UserSchema = yup.object().shape({
    username: yup
      .string()
      .min(5, "Username must be at least 5 characters")
      .max(20, "Username must be at most 20 characters")
      .test(
        "valid-chs",
        "Username may only contain letters and numbers",
        (value) => {
          return /^[A-z0-9]+$/.test(value);
        }
      )
      .required("Username is required"),
    password: yup
      .string()
      .min(10, "Password must be at least 10 characters")
      .required("Password is required"),
  });

  const formik = useFormik({
    initialValues: {
      username: "",
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
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box component="form" onSubmit={formik.handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="username"
                  label="Username"
                  name="username"
                  onChange={formik.handleChange}
                />
                <p style={{ color: "red" }}>{formik.errors.username}</p>
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
            </Grid>
            {errors ? <Error msg={errors} /> : null}
            <Button
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
    </ThemeProvider>
  );
}
