import { createContext } from "react";

const UserContext = createContext(null);

function UserProvider({ children }) {
  return <UserContext.Provider value={null}>{children}</UserContext.Provider>;
}

export { UserContext, UserProvider };
