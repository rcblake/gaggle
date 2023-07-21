import { useContext } from "react";
import { UserContext } from "./UserContext";
import { useNavigate, Link } from "react-router-dom";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import AdbIcon from "@mui/icons-material/Adb";
import { theme } from "./style";

function ResponsiveAppBar({ setCurrentUser }) {
  const currentUser = useContext(UserContext);
  const navigate = useNavigate();

  const logout = () => {
    fetch("/logout", {
      method: "DELETE",
    }).then((res) => {
      if (res.ok) {
        setCurrentUser(null);
        navigate("/logout");
      }
    });
  };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography
            variant="h4"
            noWrap
            component="a"
            href="/small-logo-no-background.png"
            sx={{
              mr: 2,

              fontWeight: 700,
              letterSpacing: ".3rem",
              textDecoration: "none",
              color: "#822907",
            }}
          >
            <img
              src="/small-logo-no-background.png"
              alt="gaggle logo"
              height="40px"
            />
            Gaggle
          </Typography>

          <Box
            color="secondary"
            sx={{
              flexGrow: 1,
              justifyContent: "flex-end",
              display: "flex",
            }}
          >
            {currentUser ? (
              <>
                <Link to="/">
                  <Button color="secondary">Home</Button>
                </Link>

                <Button onClick={logout} color="secondary">
                  Log Out
                </Button>
              </>
            ) : (
              <>
                <Link to="/login">
                  <Button color="secondary">Log In</Button>
                </Link>
                <Link to="/signup">
                  <Button color="secondary">Sign Up</Button>
                </Link>
              </>
            )}
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default ResponsiveAppBar;
