import { Auth0Provider } from "@auth0/auth0-react";
import type { AppProps } from "next/app";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <Auth0Provider
      domain="dev-iggd0fc1ms6wkjfs.us.auth0.com"
      clientId="rDK0dPGtpZhJnHJdDYs6aZyF0eAQgZ5o"
    >
      <Component {...pageProps} />
    </Auth0Provider>
  );
}
