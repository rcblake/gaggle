import {
  Button,
  Box,
  AppBar,
  Toolbar,
  Typography,
  Checkbox,
  FormControl,
  FormLabel,
  FormControlLabel,
  RadioGroup,
  Radio,
  Stack,
} from "@mui/material";
import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    mode: "light",
    primary: {
      main: "#FFA458",
    },
    secondary: {
      main: "#BA3B0A",
    },
    info: {
      main: "#BA3B0A",
    },
    success: {
      main: "#8bc34a",
    },
  },
  typography: {
    fontFamily: "Oswald",
    h1: {
      fontFamily: "Oswald",
      fontWeight: 200,
      lineHeight: 0.97,
      fontSize: "6.7rem",
    },
    fontWeightBold: 500,
    button: {
      lineHeight: 1.44,
      fontSize: "1.5rem",
      fontWeight: 600,
    },
  },
});
