import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('App file upload', () => {
  render(<App />);
  const inputFile = screen.getByTestId("input-file");
});
