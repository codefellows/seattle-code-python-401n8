// Footer.test.js
import { render, screen } from '@testing-library/react';
import Footer from '@/components/Footer';
import '@testing-library/jest-dom';

describe('Footer', () => {
  it('should render the correct text', () => {
    render(<Footer />);
    const textElement = screen.getByText(/Expert Eight Ball ©2024/i);
    expect(textElement).toBeInTheDocument();
  });

  it('should have a link to the careers page', () => {
    render(<Footer />);
    const linkElement = screen.getByRole('link', { name: /careers/i });
    expect(linkElement).toBeInTheDocument();
    expect(linkElement).toHaveAttribute('href', '/careers');
  });
});
